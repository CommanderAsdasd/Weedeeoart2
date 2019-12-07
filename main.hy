#!/usr/bin/env hy

(import [numpy [*]])
(import [moviepy [*]])
(import [weedeeo.helpers [*]])

(defn greet 
    [name]
 (print "Hello fellow" name))

; (print "I was going to code in Python syntax, but then I got Hy.")
(print (greet 'stalker))
