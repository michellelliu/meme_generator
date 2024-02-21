8#-------------IMPORTS------------------

from guizero import App, TextBox, Drawing

#-------------FUNCTIONS------------------
def draw_meme():
    meme.clear()
    meme.image(50, 0, "whatt.gif")
    
    meme.text(90, 20, top_text.value,
              color="white",
              size="30",
              font = "impact")
    
    meme.text(90, 320, bottom_text.value,
              color="white",
              size="30",
              font = "impact")

#-------------APP------------------
app = App("meme")

top_text = TextBox(app, "top text", command=draw_meme)
bottom_text = TextBox(app, "bottom text", command=draw_meme)

meme = Drawing(app, width="fill", height="fill")



draw_meme()

app.display()
