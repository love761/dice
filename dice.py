# ランダムを使うためのインポート
import random
#
import pysnooper


@pysnooper.snoop()
def main():
    # てすとだーーーーー
    print("hello world")

    # ダイスを作るぞ
    print(random.random())  # 0～1までの乱数が出る

    print(random.randint(1, 6))  # 6面ダイスを作ったよ

    # 入力したダイス
    s = input("何か文字を入れてくれ！")

    try:
        deme = int(s)
    except ValueError as e:
        print('エラーが発生したよ！')
        print('だめじゃん')
        exit()

    print(random.randint(1, deme))

    print(f'1d{deme}の結果→', random.randint(1, deme))


if __name__ == "__main__":
    main()
