import tkinter as tk
import tkinter.ttk as ttk

#項目名を配列に格納
list=["東京駅","番外編・札幌","ccc"]
#選ばれた項目の説明文も配列に格納
texts=[
        "東京駅\n左が1880年,右が現在",
        "札幌駅\n左が1998年,右が現在\n(…急に変わり過ぎでは？)",
]

def result():
    #選ばれた項目が実行された時の処理
    value=combobox.current()
    #既に表示している画像を消す
    canvas.delete('del_img')
    for i in range(len(list)):
        if i ==value:
            canvas.create_image(500,350,image=imgs[value],tag='del_img')
            #既に表示されてる文がある場合は削除
            text.delete("1.0", tk.END) 
            text.insert("1.0", '{}'.format(texts[value]))
            break

root=tk.Tk()
root.title('東京')
root.resizable(False,False)
canvas=tk.Canvas(root,width=1000,height=750,bg='silver')
canvas.pack()
#画像を配列に格納
imgs=[
        tk.PhotoImage(file='sapporo_old.png'),
        tk.PhotoImage(file='sapporo.png'),
]
#プログラム実行時、最初に画面に表示される画像
img=tk.PhotoImage(file="sapporo_old.png")
canvas.create_image(500,350,image=img,tag='del_img')
#見出し文('italic'で文字を斜体)
label=tk.Label(root,text='～東京の昔と今～',font=('ＭＳ ゴシック',25,'italic'),bg='silver')
label.place(x=350,y=50)


#項目
combobox=ttk.Combobox(root, state="readonly")
combobox=ttk.Combobox(root,values=list)
combobox.pack()
#実行ボタン
button=tk.Button(root,text='選択',command=result)
button.pack()
#tk.Textの設定    
text = tk.Text(width=25,height=4,font=("メイリオ", 12))
text.place(x=360, y=610)

root.mainloop()
