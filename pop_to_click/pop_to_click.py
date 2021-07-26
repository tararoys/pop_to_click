from talon import Module, actions, noise

noise_module = Module()

@noise_module.action_class
class NoiseActions:
    def noise_pop():
        """Invoked when the user does the pop noise."""
        print("I'm a pop star.")
        actions.mouse_click(0)


def pop_handler(blah):

    actions.user.noise_pop()

noise.register("pop", pop_handler)


