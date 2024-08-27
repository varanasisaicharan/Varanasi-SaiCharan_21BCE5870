from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from game_logic import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

game = Game()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('initialize')
def initialize_game(data):
    player = data['player']
    characters = data['characters']
    game.setup_board(player, characters)
    emit('game_state', {'board': game.board, 'current_turn': game.current_turn}, broadcast=True)

@socketio.on('move')
def handle_move(data):
    player = data['player']
    char_name = data['character']
    move = data['move']
    success, message = game.move_character(player, char_name, move)
    emit('move_result', {'success': success, 'message': message})
    if success:
        emit('game_state', {'board': game.board, 'current_turn': game.current_turn}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
    
