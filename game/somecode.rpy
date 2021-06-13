init -1 python:
    from mymodule import TheThing, TheActor, TheTool

    class SomeChildThing(TheThing):
        pass

    class SomeChildActor(TheActor):
        pass

    class SomeTool(TheTool):
        pass

    thething_i_made = SomeChildThing()
    the_actor_i_use = SomeChildActor()
    the_tool = SomeTool()


