import random
import sys

# それぞれの手を定義
HANDS = {
    1:"グー",
    2:"チョキ",
    3:"パー"
}


# ユーザーの名前を用意
def get_user_name():
    print("名前を入力してください")
    return input()


# ユーザーの手を用意
def get_user_hand(user_name: str):
    try:
        print(user_name + "さん何を出しますか？数字で入力してください。1.グー 2.チョキ 3.パー")
        hand = int(input())
        if not 1 <= hand <= 3:
            raise 
        return hand
    except:
        print("正しい手を入力してください")
        sys.exit()


# CPUの手を用意
def get_cpu_hand():
    return random.randrange(1, 3)


# hand1がhand2に対しての結果を返す
def judgement(hand1:int, hand2:int):
    if hand1 == hand2:
        return "あいこ"
    elif HANDS[hand1] == "グー" and HANDS[hand2] == "チョキ":
        return "勝ち"
    elif HANDS[hand1] == "チョキ" and HANDS[hand2] == "パー":
        return "勝ち"
    elif HANDS[hand1] == "パー" and HANDS[hand2] == "グー":
        return "勝ち"
    else:
        return "負け"


# CPU vs USER の結果を出力
def output_user_vs_result(user_name:str, result:str):
    print(user_name + "の" + result)


# CPU vs CPU の結果を出力
def output_cpu_vs_cpu_result(result: str):
    if result == "勝ち":
        print("CPU1の勝ち")
    else:
        print("CPU2の勝ち")

# USER vs USER の結果を出力
def output_user_vs_user_result(user1_name:str, user2_name:str, result: str):
    if result == "勝ち":
        print(user1_name + "の勝ち")
    else:
        print(user2_name + "の勝ち")
        
# ゲームモード1
def game_mode1():
    game_count = 1
    while(game_count <= 3):
        print(str(game_count) + "回戦目")
        cpu1_hand = get_cpu_hand() 
        cpu2_hand = get_cpu_hand()
        print("CPU1: " + HANDS[cpu1_hand] + " CPU2: " + HANDS[cpu2_hand])
        
        result = judgement(cpu1_hand, cpu2_hand)
        
        if(result == "あいこ"):
            print("あいこなのでもう一回！")
        else:
            output_cpu_vs_cpu_result(result)
            game_count += 1

# ゲームモード2
def game_mode2():
    user_name = get_user_name()

    game_count = 1
    while(game_count <= 5):
        print(str(game_count) + "回戦目")
        cpu_hand = get_cpu_hand()
        user_hand = get_user_hand(user_name)
        
        result = judgement(user_hand, cpu_hand)
        
        if(result == "あいこ"):
            print("あいこなのでもう一回！")
        else:
            output_user_vs_result(user_name, result)
            game_count += 1

# ゲームモード3
def game_mode3():
    print("1人目:", end="")
    user1_name = get_user_name()

    print("2人目:", end="")
    user2_name = get_user_name()
    
    game_count = 1
    while(game_count <= 2):
        print(str(game_count) + "回戦目")
        user1_hand = get_user_hand(user1_name)
        user2_hand = get_user_hand(user2_name)
        
        result = judgement(user1_hand, user2_hand)
        
        if(result == "あいこ"):
            print("あいこなのでもう一回！")
        else:
            output_user_vs_user_result(user1_name, user2_name, result)
            game_count += 1

        
# メインプログラム
def main():
    print("ゲームモードを選択: 1. CPU vs CPU 2. CPU vs USER 3. USER vs USER")
    game_mode = int(input())
    
    if game_mode == 1:
        game_mode1()
    elif game_mode == 2:
        game_mode2()
    elif game_mode == 3:
        game_mode3()

main()
