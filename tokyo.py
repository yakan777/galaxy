import tkinter as tk
import tkinter.ttk as ttk

#項目名を配列に格納
list=[
        "浅草",
        "秋葉原",
        "新橋",
        "日本橋",
        "渋谷",
        "新宿",
        "番外編・札幌",
]
#選ばれた項目の説明文も配列に格納
texts=[
        "【浅草】\n左が1912年頃,右が現在\n左の写真,奥に映る凌雲閣は1923年の関東大震災により倒壊,手前にある瓢箪池は1951年に埋め立てられたためこちらも現存しない",
        "【秋葉原】\n左が2000年頃,右が現在\n秋葉原といえばバスケットコートという印象の人も多くいるが,バスケットコートが存在したのは90年代半ばから01年までとわずか6年ほどである ",
        "【新橋】\n左が1965年頃,右が現在\n右の写真,左側に映るニュー新橋ビルは老朽化による耐震性の低下のため,今年の解体が発表されていたが今の所解体に向けた動きはない",
        "【日本橋】\n左が1952年頃,真ん中が1963年頃,右が現在\n現在高速道路の地下化工事が始まり,2040年に工事が完了予定\n日本橋は左の写真のように高速道路がなかった頃の景色に戻る",
        "【渋谷】\n左が1951年,右が現在\n渋谷の過去の写真でよく登場するこのケーブルカーは1951年の8月末から約1年半しか稼働していない",
        "【新宿】\n左が1963年,右が現在\n1963年の新宿西口にはまだ小田急と京王のビルがない",
        "【札幌駅】\n左が1998年頃,右が2003年以降の姿\n2000年頃までは左の写真の状態(…急に変わり過ぎでは？)",
]

def result():
    #選ばれた項目が実行された時の処理
    value=combobox.current()
    #tk.Textの設定    
    text = tk.Text(width=40,height=6,font=("メイリオ", 10))
    text.place(x=340, y=470)
    #既に表示している画像を消す
    canvas.delete('del_img')
    for i in range(len(list)):
        if i ==value:
            canvas.create_image(500,300,image=imgs[value],tag='del_img')
            #既に表示されてる文がある場合は削除
            text.delete("1.0", tk.END) 
            text.insert("1.0", '{}'.format(texts[value]))
            break

root=tk.Tk()
root.title('東京')
root.resizable(False,False)
#キャンバスの大きさ
canvas=tk.Canvas(root,width=1000,height=600,bg='silver')
canvas.pack()
#画像を配列に格納
imgs=[
        tk.PhotoImage(file='asakusa.png'),
        tk.PhotoImage(file='akihabara.png'),
        tk.PhotoImage(file='shinbashi.png'),
        tk.PhotoImage(file='nihonbashi.png'),
        tk.PhotoImage(file='shibuya.png'),
        tk.PhotoImage(file='shinjuku.png'),
        tk.PhotoImage(file='sapporo.png'),
]
#プログラム実行時、最初に画面に表示される画像
img=tk.PhotoImage(file="tokyo_tower.png")
canvas.create_image(500,300,image=img,tag='del_img')
#見出し文('italic'で文字を斜体)
label=tk.Label(root,text='～東京の昔と今～',font=('ＭＳ ゴシック',25,'italic'),bg='silver')
label.place(x=350,y=25)


#項目
combobox=ttk.Combobox(root, state="readonly")
combobox=ttk.Combobox(root,values=list)
combobox.pack()
#実行ボタン
button=tk.Button(root,text='選択',command=result)
button.pack()

root.mainloop()
