let input =
  let parse_range s =
    s
    |> String.split_on_char '-'
    |> List.map int_of_string
    |> function [a; b] -> (a, b) | _ -> failwith "parse"
  in
  open_in "day02.in"
  |> In_channel.input_all
  |> String.trim
  |> String.split_on_char ','
  |> List.map parse_range

let rec chunks n = function
  | [] -> []
  | xs -> List.take n xs :: chunks n (List.drop n xs)

let rec rows_equal = function
  | [] | [_] -> true
  | x :: y :: rem -> x = y && rows_equal (y :: rem)

let range l r = List.init (r - l + 1) (( + ) l)
let list_of_int i = List.of_seq (String.to_seq (string_of_int i))

let is_doubled n =
  let s = list_of_int n in
  let chunks = chunks ((List.length s + 1) / 2) s in
  rows_equal chunks

let is_multiplied n =
  let s = list_of_int n in
  let len = List.length s in
  List.init (len - 1) (( + ) 1)
  |> List.filter (fun n -> len mod n = 0)
  |> List.exists (fun m -> rows_equal (chunks m s))

let filter_sum pred =
  input
  |> List.concat_map (fun (l, r) -> range l r)
  |> List.filter pred
  |> List.fold_left ( + ) 0

let part1 = filter_sum is_doubled
let part2 = filter_sum is_multiplied

let () = Printf.printf "Part 1 = %d, Part 2 = %d\n" part1 part2
