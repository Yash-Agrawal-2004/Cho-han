from tkinter import *
from PIL import Image, ImageTk, ImageOps
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"

def load_image(path):
    return ImageTk.PhotoImage(Image.open(path))

def fit_image(path, width, height):
    """Resize and crop an image so it completely fills its display area."""
    if width <= 1 or height <= 1:
        return load_image(path)

    source = Image.open(path)
    resized = ImageOps.fit(
        source,
        (width, height),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    )
    return ImageTk.PhotoImage(resized)


root=Tk()
root.title("CHO - HAN GAME")
root.state("zoomed")

# Keep the original background image and resize/crop it whenever the
# maximized window changes size. This removes the white bars while
# preserving the image aspect ratio.
background_source = Image.open(ASSETS_DIR / "background.png")
img = None

label = Label(root)
label.place(relx=0, rely=0, relwidth=1, relheight=1)
label.lower()

def resize_background(event=None):
    global img

    width = root.winfo_width()
    height = root.winfo_height()

    if width <= 1 or height <= 1:
        return

    resized = ImageOps.fit(
        background_source,
        (width, height),
        method=Image.Resampling.LANCZOS,
        centering=(0.5, 0.5),
    )

    img = ImageTk.PhotoImage(resized)
    label.config(image=img)
    label.image = img

root.bind("<Configure>", resize_background)
root.update_idletasks()
resize_background()

# Heading: keep the original heading, but give it enough space and remove
# the large vertical padding that was clipping the text.
head=Label(
    root,
    text="Chō-Han (丁半)",
    pady=0,
    font=('courier',32,"bold","underline"),
    bg="#141413",
    fg="#FFFDD0",
    anchor="center",
)
head.place(relx=.5,rely=0.05,relwidth=.45,relheight=.10,anchor="n")

def resize_heading(event=None):
    width = root.winfo_width()
    if width <= 1:
        return

    # Scale the heading font with the window width so the complete
    # title remains visible at smaller and larger window sizes.
    size = max(18, min(44, int(width * 0.022)))
    head.config(font=('courier', size, "bold", "underline"))

root.bind("<Configure>", resize_heading, add="+")
root.update_idletasks()
resize_heading()


#main code
import random

CHO = "cho"
HAN = "han"

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1+die2


def get_computer_choice():

    return CHO if random.randint(0, 1) == 0 else HAN

def determine_winner(player_choice, computer_choice, dice_total):
 
    is_even = dice_total % 2 == 0
    if (is_even and player_choice == CHO and computer_choice == CHO) or (not is_even and player_choice == HAN and computer_choice == HAN):
         return "Tie"
    elif (is_even and player_choice == CHO) or (not is_even and player_choice == HAN):
        return "Player"
    elif (is_even and computer_choice == CHO) or (not is_even and computer_choice == HAN):
        return "Computer"
    else:
        return ""
     
global value
value=StringVar()
value.set("cho")
Round=StringVar()
Round.set("1")

def play():
    global label9, b1

    # Destroy the original Start button before reusing b1 for Begin.
    if b1 is not None:
        try:
            b1.destroy()
        except TclError:
            pass
        b1 = None

    label9=Label(text='Enter Number of rounds to play',font=("courier", 25),bg="#141413",fg="#FFFDD0")
    label9.place(relx=.5,rely=.3,anchor="center")

    b1=Button(text="Begin",bg="purple",fg="white",font=('courier'),command=valid,
            bd=2, relief="solid", highlightthickness=1, highlightbackground="black")
    b1.place(relx=.5,rely=.6,relwidth=.1,relheight=.05,anchor="center")
    global choice1
    
    
    choice1 =Entry(root,textvariable=Round,font=('courier',20),bg="#141413",fg="#FFFDD0",cursor="crosshair",bd=8,justify="center")
    choice1.place(relx=.5,rely=.4,relwidth=.1,relheight=.048,anchor="center")
    
    
    
def valid():
        n=Round.get()
        if(n.isnumeric()):
            global r, b1
            r=int(n)
            # Remove Begin immediately after it is clicked.
            if 'b1' in globals():
                try:
                    b1.destroy()
                    b1 = None
                except TclError:
                    pass

            play_game()
        else:
            b1=Button(text="Begin",bg="purple",fg="white",font=('courier'),command=valid,
            bd=2, relief="solid", highlightthickness=1, highlightbackground="black")
            b1.place(relx=.5,rely=.6,relwidth=.1,relheight=.05,anchor="center")
    
    
def _cleanup_winner_screen():
    """Remove every widget belonging to the final winner screen."""
    _destroy_button_border_labels()
    global winner_button
    for widget_name in ('winner_button', 'exit_button', 'label9', 'label10', 'label11', 'label100', 'label200'):
        widget = globals().get(widget_name)
        if widget is not None:
            try:
                widget.destroy()
            except TclError:
                pass
            globals()[widget_name] = None


def _start_new_game_setup():
    global label9, b1, choice1
    label9=Label(text='Enter Number of rounds to play',font=("courier", 25),bg="#141413",fg="#FFFDD0")
    label9.place(relx=.5,rely=.3,anchor="center")
    b1=Button(text="Begin",bg="purple",fg="white",font=('courier'),command=valid,
            bd=2, relief="solid", highlightthickness=1, highlightbackground="black")
    b1.place(relx=.5,rely=.6,relwidth=.1,relheight=.05,anchor="center")
    choice1=Entry(root,textvariable=Round,font=('courier',20),bg="#141413",fg="#FFFDD0",cursor="crosshair",bd=8,justify="center")
    choice1.place(relx=.5,rely=.42,relwidth=.1,relheight=.06,anchor="center")


def play_again():
    _cleanup_winner_screen()
    _start_new_game_setup()


def play_again1():
    _cleanup_winner_screen()
    _start_new_game_setup()


def play_again2():
    _cleanup_winner_screen()
    _start_new_game_setup()

player_score = 0
computer_score = 0
i=0

def _widget_is_alive(name):
    """Return True only when a global widget reference is a live Tk widget."""
    widget = globals().get(name)
    if widget is None:
        return False
    try:
        return bool(widget.winfo_exists())
    except (TclError, AttributeError):
        return False


def resize_character_images(event=None):
    """Resize character images safely while widgets are created/destroyed."""
    global img1, img2, img3, img4

    try:
        if _widget_is_alive("label20"):
            widget = globals()["label20"]
            w, h = widget.winfo_width(), widget.winfo_height()
            if w > 1 and h > 1:
                img1 = fit_image(ASSETS_DIR / "player.png", w, h)
                widget.config(image=img1)
                widget.image = img1

        if _widget_is_alive("label21"):
            widget = globals()["label21"]
            w, h = widget.winfo_width(), widget.winfo_height()
            if w > 1 and h > 1:
                img2 = fit_image(ASSETS_DIR / "bot.png", w, h)
                widget.config(image=img2)
                widget.image = img2

        if _widget_is_alive("label100"):
            widget = globals()["label100"]
            w, h = widget.winfo_width(), widget.winfo_height()
            if w > 1 and h > 1:
                img3 = fit_image(ASSETS_DIR / "player.png", w, h)
                widget.config(image=img3)
                widget.image = img3

        if _widget_is_alive("label200"):
            widget = globals()["label200"]
            w, h = widget.winfo_width(), widget.winfo_height()
            if w > 1 and h > 1:
                img4 = fit_image(ASSETS_DIR / "bot.png", w, h)
                widget.config(image=img4)
                widget.image = img4
    except (TclError, AttributeError):
        # Configure events can fire while a widget is being destroyed.
        pass


def resize_score_labels(event=None):
    """Resize score labels safely, including during screen transitions."""
    if not _widget_is_alive("p") or not _widget_is_alive("b"):
        return

    try:
        width = root.winfo_width()
        if width <= 1:
            return

        size = max(12, min(25, int(width * 0.017)))
        globals()["p"].config(font=('courier', size))
        globals()["b"].config(font=('courier', size))

        if _widget_is_alive("label6"):
            globals()["label6"].config(font=('courier', size))
        if _widget_is_alive("label7"):
            globals()["label7"].config(font=('courier', size))
    except (TclError, AttributeError):
        # Configure events can fire between destroying and recreating widgets.
        pass


def _destroy_widget(name):
    """Safely destroy a widget and clear its global reference."""
    widget = globals().get(name)
    if widget is not None:
        try:
            if widget.winfo_exists():
                widget.destroy()
        except (TclError, AttributeError):
            pass
    globals()[name] = None



def _destroy_button_border_labels():
    """Destroy separate white Label widgets used as button border/backgrounds.

    Some versions of the game used a Label underneath each Button to create
    a white border. Destroying the Button alone does not destroy that Label.
    This cleanup removes those border Labels whenever a screen/control is
    replaced. It intentionally leaves the game's normal dark Labels and
    character-image Labels untouched.
    """
    try:
        for widget in root.winfo_children():
            try:
                if widget.winfo_class() != "Label":
                    continue
                bg = str(widget.cget("bg")).lower()
                text = str(widget.cget("text"))
                image = str(widget.cget("image"))

                # The old button-border labels use Tk's default Windows
                # widget background, which is usually #f0f0f0 /
                # SystemButtonFace. They are separate Labels underneath the
                # purple buttons, so destroying the Button does not remove
                # them. Only remove light, empty Labels so normal game labels
                # and character images are never touched.
                light_backgrounds = {
                    "white", "#ffffff", "#fff", "#f0f0f0",
                    "systembuttonface", "#d9d9d9", "#e0e0e0"
                }
                if bg in light_backgrounds and text == "" and image == "":
                    widget.destroy()
            except (TclError, AttributeError):
                pass
    except (TclError, AttributeError):
        pass

def _destroy_round_widgets():
    """Destroy all widgets that belong to the current round."""
    _destroy_button_border_labels()
    for name in (
        "label3",
        "label70", "choice2", "choice3", "b4"
    ):
        _destroy_widget(name)


def _destroy_start_widgets():
    """Destroy the round-count/start screen widgets."""
    _destroy_button_border_labels()
    for name in ("label9", "choice1", "b1"):
        _destroy_widget(name)


def _destroy_game_widgets_for_restart():
    """Destroy all widgets from the old game before Play Again starts."""
    _destroy_start_widgets()
    _destroy_round_widgets()
    for name in (
        "label30", "b9", "p", "b", "label20", "label21",
        "label10", "label11", "label100", "label200", "winner_button",
        "exit_button"
    ):
        _destroy_widget(name)


def _show_scores():
    """Display exactly one current score value for each side."""
    _destroy_widget("label6")
    _destroy_widget("label7")

    label6 = Label(root, text=player_score, font=('courier', 25),
                   bg="#141413", fg="#FFFDD0")
    label6.place(relx=.03, rely=.17, anchor="w")
    globals()["label6"] = label6

    label7 = Label(root, text=computer_score, font=('courier', 25),
                   bg="#141413", fg="#FFFDD0")
    label7.place(relx=.97, rely=.17, anchor="e")
    globals()["label7"] = label7


def _create_round_screen(round_number):
    """Create one clean round screen with one selector and one Next button."""
    # Keep the current score labels and the most recently resolved player/bot
    # choices visible while creating the next round. Only transient round
    # controls are destroyed here. Scores are explicitly replaced after a
    # round is resolved, not when the next round screen is created.
    _destroy_round_widgets()

    label3 = Label(root, text='ROUND ' + str(round_number) + ' BEGINS',
                   font=("courier", 25), bg="#141413", fg="#FFFDD0")
    label3.place(relx=.5, rely=.3, anchor="center")
    globals()["label3"] = label3

    label70 = Label(root, text='Pick your choice', font=("courier", 20),
                    bg="#141413", fg="#FFFDD0")
    label70.place(relx=.5, rely=.36, anchor="center")
    globals()["label70"] = label70

    choice2 = OptionMenu(root, value, "cho", "han")
    choice2.config(font=('courier', 20), bg="#141413", fg="#FFFDD0",
                   cursor="crosshair", bd=8, justify="center", width=5)
    choice2.place(relx=.5, rely=.42, width=125, height=55, anchor="center")
    globals()["choice2"] = choice2

    b4 = Button(root, text="Next", bg="purple", fg="white", font=('courier'),
                command=rounds,
                bd=2, relief="solid", highlightthickness=1,
                highlightbackground="black")
    b4.place(relx=.5, rely=.6, relwidth=.1, relheight=.05, anchor="center")
    globals()["b4"] = b4


def _resolve_current_round():
    """Resolve the current selection and show its result without duplicates."""
    global player_score, computer_score, label4, label5, label8

    # Remove all choice/round-start widgets before showing the result.
    _destroy_widget("label3")
    _destroy_widget("label70")
    _destroy_widget("choice2")
    _destroy_widget("choice3")
    _destroy_widget("label4")
    _destroy_widget("label5")
    _destroy_widget("label8")

    player_choice = value.get()
    computer_choice = get_computer_choice()
    dice_total = roll_dice()
    winner = determine_winner(player_choice, computer_choice, dice_total)

    label4 = Label(root, text=player_choice, font=('courier', 20),
                   bg="#141413", fg="#FFFDD0")
    label4.place(relx=.31, rely=.735, anchor="center")
    globals()["label4"] = label4

    label5 = Label(root, text=computer_choice, font=('courier', 20),
                   bg="#141413", fg="#FFFDD0")
    label5.place(relx=.728, rely=.735, anchor="center")
    globals()["label5"] = label5

    if winner == "Player":
        player_score += 1
    elif winner == "Computer":
        computer_score += 1
    elif winner == "Tie":
        player_score += 1
        computer_score += 1

    _show_scores()

    japanese_numbers = {
        1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU',
        7: 'SHICHI', 8: 'HACHI', 9: 'KYU', 10: 'JUU',
        11: 'JU ICHI', 12: 'JU NI'
    }
    label8 = Label(
        root,
        text="Sum was " + japanese_numbers[dice_total] + "(" + str(dice_total) + ")",
        font=('courier', 25), bg="#141413", fg="#FFFDD0"
    )
    label8.place(relx=.5, rely=.5, anchor="center")
    globals()["label8"] = label8


def rounds():
    """Process one Next click and move to the next clean round or GAME OVER."""
    global i, label30, b9

    # Next is a one-click control. Destroy it and its separate white border
    # Label before rendering the round result.
    _destroy_widget("b4")
    _destroy_button_border_labels()

    _resolve_current_round()

    # ``i`` is zero-based (round 1 == i=0).  Therefore the current
    # round is the final round when i + 1 reaches the requested total.
    if i + 1 >= r:
        # Final round: no selector, Next button, round label, or old result
        # control may remain behind GAME OVER.
        _destroy_widget("label3")
        _destroy_widget("label70")
        _destroy_widget("choice2")
        _destroy_widget("choice3")
        # Keep the resolved player/bot choices visible on the GAME OVER
        # screen. They were already created by _resolve_current_round()
        # immediately above and are positioned beside the character images.
        # Do NOT destroy label4/label5 here. They are removed later by
        # winners() when the final winner screen is displayed.

        label30 = Label(root, text="GAME OVER", font=("courier", 25),
                        bg="#141413", fg="#FFFDD0")
        label30.place(relx=.5, rely=.3, anchor="center")
        globals()["label30"] = label30

        b9 = Button(root, text="Winner", bg="purple", fg="white",
                    font=('courier'), command=winners,
                    bd=2, relief="solid", highlightthickness=1,
                    highlightbackground="black")
        b9.place(relx=.5, rely=.6, relwidth=.1, relheight=.05, anchor="center")
        globals()["b9"] = b9
        return

    # There are more rounds. Remove the previous round's result completely,
    # increment the round number, and create one fresh round screen.
    # Keep the just-resolved player/bot choices visible beside their images
    # while the next round is being played. On the next Next click,
    # _resolve_current_round() replaces these labels with the new choices.
    _destroy_widget("label6")
    _destroy_widget("label7")

    # The score must be visible during EVERY round.  Create fresh score
    # labels after the previous round's labels have been destroyed, using
    # the already-updated scores from _resolve_current_round().
    _show_scores()

    i += 1
    _create_round_screen(i + 1)


def play_game():
    """Start a clean multi-round game."""
    global i, player_score, computer_score, p, b, label20, label21

    _destroy_start_widgets()
    _destroy_round_widgets()

    i = 0
    player_score = 0
    computer_score = 0

    # Remove any old score headings/images from a previous Play Again.
    for name in ("p", "b", "label20", "label21", "label30", "b9"):
        _destroy_widget(name)

    p = Label(root, text="Player Score", font=('courier', 25),
              bg="#141413", fg="#FFFDD0")
    p.place(relx=0.03, rely=.1, anchor="w")
    globals()["p"] = p

    b = Label(root, text="Bot Score", font=('courier', 25),
              bg="#141413", fg="#FFFDD0")
    b.place(relx=.97, rely=.1, anchor="e")
    globals()["b"] = b

    img1 = load_image(ASSETS_DIR / "player.png")
    label20 = Label(root, image=img1, bg="#141413")
    label20.place(relx=.25, rely=.78, relwidth=.12, relheight=.235)
    globals()["label20"] = label20
    globals()["img1"] = img1

    img2 = load_image(ASSETS_DIR / "bot.png")
    label21 = Label(root, image=img2, bg="#141413")
    label21.place(relx=.668, rely=.78, relwidth=.12, relheight=.235)
    globals()["label21"] = label21
    globals()["img2"] = img2

    root.update_idletasks()
    resize_character_images()

    # Scores start at zero and only one score label exists for each side.
    # These labels must remain visible while every round screen is created.
    _show_scores()
    resize_score_labels()

    # Exactly one selector and one Next button are created for round 1.
    _create_round_screen(1)


def exit_game():
    """Close the game window."""
    root.destroy()


def _create_exit_button():
    """Create the red Exit button below Play again on the winner screen."""
    global exit_button

    _destroy_widget("exit_button")

    exit_button = Button(
        root,
        text="Exit",
        bg="red",
        fg="white",
        font=('courier', 16),
        command=exit_game,
        bd=2,
        relief="solid",
        highlightthickness=1,
        highlightbackground="black"
    )
    exit_button.place(
        relx=.5,
        rely=.68,
        width=150,
        height=55,
        anchor="n"
    )


def winners():
    _destroy_button_border_labels()
    global label30, label9, label10, label11, label100, label200, winner_button, b9, b4, b1

    # Remove any Start/Begin button that may still exist.
    if b1 is not None:
        try:
            b1.destroy()
        except TclError:
            pass
        b1 = None

    # Remove the previous round's Next button.
    if globals().get('b4') is not None:
        try:
            b4.destroy()
        except (TclError, AttributeError):
            pass
        b4 = None
    _destroy_button_border_labels()

    # Remove the previous screen's Winner button.
    if globals().get('b9') is not None:
        try:
            b9.destroy()
        except (TclError, AttributeError):
            pass
        b9 = None

    # Remove the GAME OVER screen before showing the final winner screen.
    if 'label30' in globals():
        try:
            label30.place_forget()
        except TclError:
            pass

    # Remove the score/result widgets from the previous screen.
    for widget_name in ('label6', 'label7', 'label20', 'label21',
                        'label4', 'label5', 'label8', 'p', 'b',
                        'choice1', 'choice2', 'choice3', 'label70'):
        widget = globals().get(widget_name)
        if widget is not None:
            try:
                widget.place_forget()
            except TclError:
                pass

    if player_score > computer_score:
        label9=Label(root,text="Winner!",font=('courier',20),
                     bg="#141413",fg="#FFFDD0")
        label9.place(relx=.5,rely=.29,anchor="center")

        img3=load_image(ASSETS_DIR / "player.png")
        label100=Label(root,image=img3,bg="#141413")
        label100.place(relx=.5,rely=.35,width=180,height=180,anchor="n")

        winner_button=Button(root,text="Play again",bg="purple",fg="white",
                             font=('courier',16),command=play_again,
                             bd=2,relief="solid",highlightthickness=1,
                             highlightbackground="black")
        winner_button.place(relx=.5,rely=.60,width=150,height=55,anchor="n")
        _create_exit_button()

    elif computer_score > player_score:
        label10=Label(root,text="Winner!",font=('courier',20),
                      bg="#141413",fg="#FFFDD0")
        label10.place(relx=.5,rely=.29,anchor="center")

        img4=load_image(ASSETS_DIR / "bot.png")
        label200=Label(root,image=img4,bg="#141413")
        label200.place(relx=.5,rely=.35,width=180,height=180,anchor="n")

        winner_button=Button(root,text="Play again",bg="purple",fg="white",
                             font=('courier',16),command=play_again1,
                             bd=2,relief="solid",highlightthickness=1,
                             highlightbackground="black")
        winner_button.place(relx=.5,rely=.60,width=150,height=55,anchor="n")
        _create_exit_button()

    else:
        label11=Label(root,text="Both are winners!",font=('courier',20),
                      bg="#141413",fg="#FFFDD0")
        label11.place(relx=.5,rely=.29,anchor="center")

        img3=load_image(ASSETS_DIR / "player.png")
        label100=Label(root,image=img3,bg="#141413")
        label100.place(relx=.38,rely=.35,width=150,height=150,anchor="n")

        img4=load_image(ASSETS_DIR / "bot.png")
        label200=Label(root,image=img4,bg="#141413")
        label200.place(relx=.62,rely=.35,width=150,height=150,anchor="n")

        winner_button=Button(root,text="Play again",bg="purple",fg="white",
                             font=('courier',16),command=play_again2,
                             bd=2,relief="solid",highlightthickness=1,
                             highlightbackground="black")
        winner_button.place(relx=.5,rely=.60,width=150,height=55,anchor="n")
        _create_exit_button()



# Keep character images and score headings responsive when the
# window is resized.
root.bind("<Configure>", resize_character_images, add="+")
root.bind("<Configure>", resize_score_labels, add="+")

#start button
b1=None
exit_button=None
b1=Button(text="Start",bg="purple",fg="white",font=('courier'),command=play,
            bd=2, relief="solid", highlightthickness=1, highlightbackground="black")
b1.place(relx=.5,rely=.6,relwidth=.1,relheight=.05,anchor="center")

root.mainloop()
