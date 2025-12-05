(ns day04
  (:require [clojure.string :as str]))

(defn parse-passport [line]
  (->>
   (str/split line #"\s")
   (map #(str/split % #":"))
   (map (fn [[k v]] [(keyword k) v]))
   (into {})))

(defn parse-input [path]
  (->>
   (str/split (slurp path) #"\n\n")
   (map parse-passport)))

(defn part-1 [input]
  (let
   [required-fields [:byr :iyr :eyr :hgt :hcl :ecl :pid]]
    (count
     (filter
      (fn [line] (every? #(contains? line %) required-fields))
      input))))

(defn part-2 [input]
  (count (filter valid-passport? input)))

(def input (parse-input "day04.in"))
(time (part-1 input))

(time (part-2 input))
