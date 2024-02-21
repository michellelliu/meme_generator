8#-------------IMPORTS------------------

from guizero import App, TextBox, Drawing, Combo, Slider

#-------------FUNCTIONS------------------
def draw_meme():
    meme.clear()
    meme.image(50, 0, "whatt.gif")
    
    meme.text(90, 20, top_text.value,
              color=color.value,
              size= size.value,
              font = font.value)
    
    meme.text(90, 320, bottom_text.value,
              color=color.value,
              size= size.value,
              font = font.value)

#-------------APP------------------
app = App("meme")

app.bg = "white"

top_text = TextBox(app, "top text", command=draw_meme)
bottom_text = TextBox(app, "bottom text", command=draw_meme)

color = Combo(app,
              options = ["black", "white", "red", "green", "blue", "orange"],
              command = draw_meme,
              selected = "white")

font = Combo(app,
             options = ["times new roman", "verdana", "courier", "impact"],
             command = draw_meme,
             selected = "impact")

size = Slider(app, start=20, end=40, command=draw_meme)

meme = Drawing(app, width="fill", height="fill")



draw_meme()

app.display()
