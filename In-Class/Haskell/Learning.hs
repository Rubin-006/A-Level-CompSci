import Data.List
main :: IO()

fac :: Int -> Int
fac n = aux n 1
 where
    aux n acc
     | n <= 1 = acc
     | otherwise = aux (n-1) (n*acc)

                     



main = do
    val1 <- readLn
    let result = fac val1
    print result