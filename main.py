import curses

def main(stdscr):
    curses.curs_set(0)  # Cursor ni yashirin
    stdscr.clear()

    while True:
        stdscr.addstr(0, 0, "Menyu:")
        stdscr.addstr(1, 0, "1. Boshlash")
        stdscr.addstr(2, 0, "2. Chiqish")
        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Boshlash")
            stdscr.refresh()
            curses.napms(2000)  # 2 sekund ichida menyuga qaytish
        elif key == ord('2'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Chiqish")
            stdscr.refresh()
            curses.napms(2000)  # 2 sekund ichida menyuga qaytish
        elif key == ord('q'):
            break

curses.wrapper(main)
```

Bu kodda, `curses` moduli yordamida oddiy menyuli terminal dastur yaratilgan. Menyu ichida ikkita funktsiya mavjud: "Boshlash" va "Chiqish". "Boshlash" funktsiyasi 2 sekund ichida menyuga qaytadi, "Chiqish" funktsiyasi esa dasturning tugashini belgilaydi. Menyu ichida "q" tugmasi boshqa funktsiyalarni tugatish uchun ishlatiladi.
