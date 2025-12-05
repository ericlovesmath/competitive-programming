(ns day05
  (:require [clojure.string :as str]))

(defn to-binary
  ([xs] (to-binary 0 xs))
  ([acc xs]
   (cond
     (empty? xs)  acc
     (first xs) (to-binary (inc (* acc 2)) (rest xs))
     :else      (to-binary (* acc 2) (rest xs)))))

(defn parse-line [line]
  (let
   [[row col] (split-at 7 line)
    row' (map #(= % \B) row)
    col' (map #(= % \R) col)]
    [(to-binary row') (to-binary col')]))

(defn parse-input [path]
  (->>
   (slurp path)
   str/split-lines
   (map parse-line)))

(def input (parse-input "day05.in"))

(def seats (sort (map (fn [[r c]] (+ (* r 8) c)) input)))

(time (apply max seats))
(time
 (some #(when-not (contains? (set seats) %) %)
       (range (apply min seats) (apply max seats))))
