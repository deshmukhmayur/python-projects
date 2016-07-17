#!/usr/bin/python3



class Game:

    def __init__(self, master):
        self.WORDS = {'Colors':'red;orange;yellow;green;blue;indigo;violet;white;black;brown'.split(';'),
                      'Shapes':'line;triangle;square;rectangle;rhombus;trapezoid;pentagon;hexagon;heptagon;octagon;circle;ellipse'.split(';'),
                      'Fruits':'apple;orange;lemon;lime;pear;watermelon;grape;grapefruit;cherry;banana;cantaloupe;mango;strawberry;tomato'.split(';'),
                      'Animals':'bat;bear;beaver;cat;cougar;crab;deer;dog;donkey;duck;eagle;fish;frog;goat;leech;lion;lizard;llama;monkey;moose;otter;owl;panda;python;rabbit;rat;shark;sheep;skunk;squid;tiger;turkey;turtle;weasael;whale;wolf;wombat;zebra'.split(';'),
                      'Comic Book Movies':'Iron Man;The Incredible Hulk;Iron Man II;Thor;Thor: The Dark World;Captain America: The First Avenger;Marvel\'s The Avengers;'.split(';')
