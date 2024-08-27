const socket = io.connect('http://localhost:5000');

socket.on('connect', function() {
    // Setup game for player A or B
    socket.emit('initialize', { player: 'A', characters: ['P1', 'H1', 'H2', 'P2', 'P3'] });
});

socket.on('game_state', function(data) {
    renderBoard(data.board);
    document.getElementById('turn-indicator').innerText = `Current Turn: Player ${data.current_turn}`;
});

socket.on('move_result', function(data) {
    alert(data.message);
});

function renderBoard(board) {
    const boardDiv = document.getElementById('board');
    boardDiv.innerHTML = ''; // Clear the board
    for (let row = 0; row < board.length; row++) {
        for (let col = 0; col < board[row].length; col++) {
            const cell = document.createElement('div');
            cell.innerText = board[row][col];
            boardDiv.appendChild(cell);
        }
    }
}

