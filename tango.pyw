from numpy.core.numeric import False_
import pandas as pd
import tkinter as tk
from tkinter import messagebox
import random


tango_csv = 'C:/Users/jumpe/myfile/babys/Python/tango/tango.csv'
df = pd.read_csv(tango_csv,encoding='shift-jis')

# nanに0を代入
df = df.fillna(0)

df_rnd = df[df['正答率'] == df['正答率'].min()] #正答率低いやつら
print(df_rnd)
tango_rnd = round(random.uniform(0,len(df_rnd)-1)) #ランダム数値

df_new = df_rnd[tango_rnd:tango_rnd+1] #ランダムなデータフレーム
tg_index = int(df_new.index[0])

question = df_new.iat[0,0] #正答率の一番小さい単語
Answer = df_new.iat[0,1] #正答率の一番小さい意味

print(question)
print(Answer,'\n')


# 正解したか？
tk.Tk().withdraw() #小さなウィンドウを表示させない
def func_mondai(aaa,bbb):
    res = messagebox.showinfo('これは何ですか？', aaa)
    # メッセージボックス（はい・いいえ） 
    ret = messagebox.askyesno('title', f'正解は\n\n{aaa}\n{bbb}\n\nでした！')
    if ret == True:
        return 1
    else:
        return 0


cor = df.at[tg_index,'正解']
miss = df.at[tg_index,'失敗']

kaitou = func_mondai(question,Answer)

# もし正解したら正解＋１
if kaitou == 1:
    cor += 1
    #正答率再計算（正答率＝正解/（正解＋失敗））
    df.at[tg_index,'正答率'] = round(cor / (cor + miss))

else:
    miss += 1
    #正答率再計算（正答率＝正解/（正解＋失敗））
    df.at[tg_index,'正答率'] = round(cor / (cor + miss))

df.to_csv(tango_csv,encoding='shift-jis',index=False)
