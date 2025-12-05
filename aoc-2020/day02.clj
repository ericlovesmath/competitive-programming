(ns day02
  (:require [clojure.string :as str]))

(defn parse-line [line]
  (let [[_ min max letter password] (re-matches #"(\d+)-(\d+) (\w): (\w+)" line)]
    {:min (parse-long min)
     :max (parse-long max)
     :letter (first letter)
     :password password}))

(defn parse-input [path]
  (map parse-line (str/split (slurp path) #"\n")))

(defn count-pred [f xs] (count (filter f xs)))

(defn check-row-1
  [{:keys [min max letter password]}]
  (->>
    password
    (count-pred #(= % letter))
    (#(and (<= min %) (<= % max)))))

(defn check-row-2
  [{:keys [min max letter password]}]
  (->>
   [min max]
   (count-pred #(= (nth password (dec %)) letter))
   (= 1)))

(def input (parse-input "day02.in"))
(time (count-pred check-row-1 input))
(time (count-pred check-row-2 input))
