from mutators.mutator import Mutator
from genomes.genome import Genome
from typing import Tuple

class ZeroOrderDirect(Mutator):
    def __init__(self, *args) -> None:
        super().__init__(*args)

    def mutate(self, **kwargs) -> Tuple[Genome, Genome]:
        unit = {
            'mutation_prompt': self.random.choice(self.mutation_prompts),
            'thinking_style': self.random.choice(self.thinking_styles),
            'task_description': self.task_description
        }
        # TODO: Finish mutate function