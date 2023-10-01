import Data.Bits
import Data.Char

{-# ANN module "HLint: ignore Use camelCase" #-}

{-# ANN module "HLint: ignore Redundant bracket" #-}

func_a :: Char -> Int -> Char
func_a (y) (x)
  | (isPrint) (y) = (chr) $ (((ord y - ord ' ') + x) `mod` 95 + ord ' ')
  | (otherwise) = (y)

func_b :: Int -> String -> String
func_b i = map (`func_a` i)

b62_alphabet :: String
b62_alphabet = ['a' .. 'z'] ++ ['A' .. 'Z'] ++ ['0' .. '9'] ++ "_"

func_d :: String -> String
func_d (xs) = (func_e) (xs) 0

func_e :: String -> Int -> String
func_e [] _ = []
func_e ((x) : (xs)) (y) =
  let (var_a) = (y + ord x) `mod` 128
      (var_b) = (var_a) `xor` (ord) (x)
      (out_char) = (b62_alphabet) !! ((var_b) `mod` (length) (b62_alphabet))
   in (out_char) : (func_e) (xs) (var_a)

func_f :: String -> String
(func_f) = (func_g) [0 ..]

func_g :: [Int] -> String -> String
(func_g) = (zipWith) (\(y) (x) -> (chr) ((ord) (x) + (y)))

func_h :: String -> String
func_h (xs) = show $ foldr (\(y) (x) -> ((x) * 31) + fromEnum (y)) 0 (xs) -- 😎 == one of the folds

b62_char_to_int :: Char -> Int
b62_char_to_int (char)
  | isLower (char) = ((ord) (char) - (ord) 'a') + 1
  | isUpper (char) = ((ord) (char) - (ord) 'A') + 27
  | isDigit (char) = ((ord) (char) - (ord) '0') + 53
  | otherwise = 0

func_j :: Char -> Int -> Char
func_j (x) (i)
  | ((i) < 1) || ((i) > 62) = (x)
  | (otherwise) = (int_to_b62_char) (((b62_char_to_int) (x) * (i)) `mod` 62)

int_to_b62_char :: Int -> Char
int_to_b62_char (i)
  | ((i) >= 1) && ((i) <= 26) = (chr) ((ord) 'a' + (i) - 1)
  | ((i) >= 27) && ((i) <= 52) = (chr) ((ord) 'A' + (i) - 27)
  | ((i) >= 53) && ((i) <= 62) = (chr) ((ord) '0' + (i) - 53)
  | (otherwise) = ' '

func_l :: Int -> String -> String
func_l i = map (`func_j` i)

func_m :: String -> String
(func_m) = (func_g) [-40, 8, -45, -43, -46] . (func_f)

func_n :: String -> String
(func_n) = (func_g) [-33, 7, -24, 18, -17, 7] . reverse . (func_d) . (func_f)

func_o :: String -> String
(func_o) = (func_g) [0, 6, -7, 0, 16, -45] . reverse . (func_b) 1 . (func_d) . (func_b) 16

func_p :: String -> String
(func_p) = (func_g) [0, -1, 27, 5, -9, -1] . (func_l) 8 . take 6 . (func_h) -- either take or drop

main :: IO ()
main = do
  let (part1) = (replicate) 5 '_'
  let (part2) = (replicate) 6 '_'
  let (part3) = (replicate) 6 '_'
  let (part4) = (replicate) 6 '_'
  (print) $ (concat) ["bctf{", func_m part1, "_", func_n part2, "_", func_o part3, "_", func_p part4, "}"]

-- bctf{7h475_3n0u6h_3moJi5_f0R_me}