from countdown_solvers import NumberGame, AsyncNumberGame
import asyncio

if __name__ == "__main__":

    def timeit(game1:AsyncNumberGame, game2:NumberGame):
        import datetime

        async def test1(game:AsyncNumberGame):
            date = datetime.datetime.now()
            print("~"*20, "\nAsync")
            print(*(await game.get_all()), sep="\n")
            print("Time:", datetime.datetime.now() - date)
            print("~" * 20)

        def test2(game:NumberGame):
            date = datetime.datetime.now()
            print("~"*20, "\nSync")
            print(game.get_any())
            print("Time:", datetime.datetime.now() - date)
            print("~" * 20)

        #loop = asyncio.get_event_loop()
        #loop.run_until_complete(test1(game1))
        test2(game2)

    timeit(AsyncNumberGame([75, 50, 9, 1, 4, 2], 777), NumberGame([100, 75, 10, 6, 7, 10], 363))