from countdown_solvers import TextGame
import asyncio

if __name__ == "__main__":

    game = TextGame(["a", "b", "c", "d", "e", "f", "g", "h"])
    print(game.get_best())
    print(game.get_all(from_smaller=True))

    async def test():
        game1 = TextGame(["g", "r", "e", "q", "a", "c", "u", "n"])
        print(*game1.get_all(), sep="\n")

    asyncio.get_event_loop().run_until_complete(test())
