import tkinter
font = ('Times New Roman',40)
def マウス(e):
    canvas.delete('all')
    s = '({},{})'.format(e.x,e.y)
    canvas.create_text(300,200,text=s,font=font)
window=tkinter.Tk()
window.title('マウスポインタの座標')
window.bind('<Motion>',マウス)
canvas=tkinter.Canvas(width=600,height=400)
canvas.create_text(300,200,text='ウィンドウ内でマウスを動かしてください')
canvas.pack()
window.mainloop()
