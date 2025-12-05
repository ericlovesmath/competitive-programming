(ns day03
  (:require [clojure.string :as str]))

(defn parse-input [path]
  (->>
    (slurp path)
    str/split-lines
    (mapv #(mapv (fn [c] (= c \#)) %))))

(defn check-slope
  ([input dx dy] (check-slope input dx dy 0 0))
  ([input dx dy x y]
   (let
    [check #(check-slope input dx dy %1 %2)
     height (count input)
     width (count (first input))
     x' (mod (+ x dx) width)
     y' (+ y dy)]
     (cond
       (>= y' height) 0
       (nth (nth input y') x') (inc (check x' y'))
       :else (check x' y')))))

(defn part-1
  [input]
  (check-slope input 3 1))

(defn part-2
  [input]
  (*
    (check-slope input 3 1)
    (check-slope input 1 1)
    (check-slope input 5 1)
    (check-slope input 7 1)
    (check-slope input 1 2)))

(def input (parse-input "day03.in"))
(time (part-1 input))
(time (part-2 input))
