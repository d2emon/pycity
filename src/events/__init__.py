"""
Global events system

Basic events can:

* Initialize
  * handlers - dictionary of event handlers
* Emit
  * event-type - event code
  * Sends event eith event_type to every registered listener
  * Run handler by event_code
* Process events - emit every event from list
  * events - events to emit

Basic events used by:

* windows
  * screen
* games.breakout.menu_screen.groups.menu_items

Window events has events:

* INIT
* UPDATE
* DRAW

Window events can:

* Init window - emit INIT event
* Process events - emit every event from list
  * events - events to emit
  * Emit UPDATE event
  * Emit DRAW event

Game events has window events and:

* KEY
* KEY_DOWN
* KEY_UP
* MOUSE_MOTION
* MOUSE_BUTTON_DOWN
* MOUSE_BUTTON_UP
* GAME_MOUSE_MOTION
* GAME_MOUSE_BUTTON_DOWN
* GAME_MOUSE_BUTTON_UP
* QUIT

Game events used by:

* games
  * breakout.events
  * map_walk.sceens.main
  * walker.sceens.main

"""
