# Fullstack Nanodegree Projects

This repository contains multiple projects from the Udacity's Fullstack Nanodegree organized into a Vagrant VM.

## Installation Instructions

To install we simply clone this repository and let Vagrant do the VM install and provisioning.

```shell
git clone https://github.com/tomca32/fullstack-nanodegree-vm.git
cd fullstack-nanodegree-vm/vagrant
vagrant up
#... wait for a while...
```

## P2 Tournament Results

### Testing

To run the tests we need to ssh into a running vagrant instance, seed the database and run test script

```shell
vagrant ssh
cd /vagrant
./seed.sh
python tournament
```

### Functionality

Contains all the basic functionality required by the original test suite and contains additional functionality:

- tournament can handle odd number of players. In this case one of tuples in the list from swissPairings() is going to return a tuple containing one player. This there are no API changes.

### DB Design

There are only 2 tables in the database: players and matches:

- players has two columns, id (primary key) and name
- matches has three columns, id (primary key), players (array of players participating in the match)* and winner which is an id of the winner and is a foreign key referencing the id in the players table

*I wanted to make the elements of this array foreign keys referencing the players table but it seems that it cannot be done: http://dba.stackexchange.com/questions/60132/foreign-key-constraint-on-array-member

There are also 3 views:

- wins_by_player returns three columns: player id, player name and number of wins sorted by number of wins descendingly
- matches_by_player returns three columns: player id, player name and number of played matches sorted by number of matches descendingly
- player_standings returns four columns: player id, player name, number of wins and number of matches played