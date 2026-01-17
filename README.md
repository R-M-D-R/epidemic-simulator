# Epidemic Simulator

How does an infectious disease spread through a population?

This project simulates the spread of a disease using bouncing balls to represent people. When an infected ball collides with a healthy one, the healthy individual becomes sick. The simulation allows users to experiment with key variables and observe how small changes affect the course of an outbreak.

The simulation visualizes the population over time using a stacked area chart. The chart’s height represents 100% of the population, and the colors indicate the proportions of healthy, sick, recovered, and deceased individuals. Hover over the chart to see detailed population statistics at any moment.

## Motivation

I wanted to create a visual, interactive model to explore disease dynamics. This project helps demonstrate how contagiousness, illness duration, mortality, and population size influence outbreaks — all without relying on abstract equations alone.

## Features

- Adjustable incubation period (infected but asymptomatic and contagious)
- Configurable infection duration
- Settable mortality rate
- Variable population size (default: 100 people)
- Real-time visualization with stacked area chart showing healthy, sick, recovered, and deceased proportions

### Technologies

- Python
- Pygame
