# David's Space Invaders Clone

## Overview

- This is a simple Space Invaders clone without any bells and whistles.
- Goal of this project was to quickly understand the basics of [pygame](https://www.pygame.org/) and evaluate if it's suitable for further prototyping for **LLM + Games**.
- My opinion: Pygame seems great because it's simple and light weight. It's very easy to understand how everything works and hack something together. Of course, for more involved use cases there will be limitations. I will continue leveraging it for more involved experiments.

## How to play

Defeat the space invaders by moving the ship left (←) and right (→) and shooting (Space).

![Project Demo](./animated_gif.gif)

## Installation

To install the necessary dependencies, first install conda, for example [miniconda](https://docs.anaconda.com/free/miniconda/). Then run:

```bash
make create_env
```

Afterwards run:

```bash
conda activate pygame_1
```

And finally run:

```bash
make run
```
