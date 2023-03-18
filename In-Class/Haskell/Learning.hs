import Data.List
main :: IO()

fac :: Int -> Int
fac n = aux n 1 -- Factorial Function
 where
    aux n acc
     | n <= 1 = acc
     | otherwise = aux (n-1) (n*acc)



f :: [Int] -> [Int]
let counter = 0

f (x:lst) =
    if count % 2 == 0
        then x = x
            let count = count + 1
            head lst
            f lst
        head lst
        f lst
                     



main = do
    let lst = [1,2,3,4,5]
    let result = f lst
    print result