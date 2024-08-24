import chess
import chess.engine
from colorama import Fore, Style, init

init()

def print_chess_board(board):
    symbols = {
        chess.PAWN: black + 'P' + reset, chess.KNIGHT: blue + 'N' + reset, chess.BISHOP: cyan + 'B' + reset,
        chess.ROOK: green + 'R' + reset, chess.QUEEN: pink + 'Q' + reset, chess.KING: yellow + 'K' + reset
    }

    print("  a b c d e f g h")
    for rank in range(8):
        print(f"{8 - rank} ", end=" ")
        for file in range(8):
            piece = board.piece_at(chess.square(file, 7 - rank))
            if piece:
                print(symbols[piece.piece_type] if piece.color == chess.WHITE else symbols[piece.piece_type].lower(), end=" ")
            else:
                print(".", end=" ")
        print()
    print("  a b c d e f g h")

def get_user_move(board):
    move = input(green + "[>] Введите ваш ход: " + reset)
    try:
        move = chess.Move.from_uci(move)
        if move in board.legal_moves:
            return move
        else:
            print(red + "[!] Недопустимый ход." + reset)
            return get_user_move(board)
    except:
        print(red + "[!] Ошибка ввода. Попробуйте еще раз." + reset)
        return get_user_move(board)

def main():
    stockfish_path = r"..\chesshack\stockfish\stockfish-windows-x86-64-avx2.exe"

    board = chess.Board()
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

    color_choice = input(green + "[?] Выберите цвет (белый/черный): " + reset).strip().lower()
    player_color = chess.WHITE if color_choice == 'белый' else chess.BLACK
    player_turn = player_color == chess.WHITE

    print(green + "[+] Игра началась!" + reset)
    print_chess_board(board)

    while not board.is_game_over():
        if player_turn:
            user_move = get_user_move(board)
            board.push(user_move)
        else:
            result = engine.play(board, chess.engine.Limit(time=2.0))
            board.push(result.move)
            print(green + f"[%] ChessHack предлагает следующий ход: {result.move}" + reset)
            print_chess_board(board)

        player_turn = not player_turn

    print(yellow + "[&] Игра окончена. Результат:", board.result() + reset)
    engine.quit()

text = """ ▄▀▄▄▄▄   ▄▀▀▄ ▄▄   ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄  ▄▀▀▀▀▄  ▄▀▀▄ ▄▄   ▄▀▀█▄   ▄▀▄▄▄▄   ▄▀▀▄ █
█ █    ▌ █  █   ▄▀ ▐  ▄▀   ▐ █ █   ▐ █ █   ▐ █  █   ▄▀ ▐ ▄▀ ▀▄ █ █    ▌ █  █ ▄▀
▐ █      ▐  █▄▄▄█    █▄▄▄▄▄     ▀▄      ▀▄   ▐  █▄▄▄█    █▄▄▄█ ▐ █      ▐  █▀▄ 
  █         █   █    █    ▌  ▀▄   █  ▀▄   █     █   █   ▄▀   █   █        █   █
 ▄▀▄▄▄▄▀   ▄▀  ▄▀   ▄▀▄▄▄▄    █▀▀▀    █▀▀▀     ▄▀  ▄▀  █   ▄▀   ▄▀▄▄▄▄▀ ▄▀   █ 
█     ▐   █   █     █    ▐    ▐       ▐       █   █    ▐   ▐   █     ▐  █    ▐ 
▐         ▐   ▐     ▐                         ▐   ▐            ▐        ▐      """

green = Fore.GREEN + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
pink = Fore.MAGENTA + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
black = Fore.BLACK + Style.BRIGHT
reset = Style.RESET_ALL

if __name__ == "__main__":
    print(green + text + reset)
    print(green + "\n[$] Автор: raccoon888\n" + reset)
    main()
