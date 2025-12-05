(ns day01
  (:require [clojure.string :as str]))

(defn parse-input [path]
  (map parse-long (str/split (slurp path) #"\n")))

(defn part-1 [input]
  (let
   [input-set (set input)
    x (some #(when (contains? input-set (- 2020 %)) %) input)]
    (* x (- 2020 x))))

(defn part-2 [input]
  (let [s (set input)]
    (some (fn [x]
            (let [remaining (- 2020 x)]
              (some (fn [y]
                      (let [z (- remaining y)]
                        (when (s z) (* x y z))))
                    (remove #{x} input))))
          input)))

(def input (parse-input "day01.in"))
(time (part-1 input))
(time (part-2 input))
