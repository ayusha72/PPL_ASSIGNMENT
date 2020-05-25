;;;Factorial without recursion

(defun fact_norm (n)
   (let ((f 1))
      (dotimes (i n) 
         (setf f (* f (+ i 1))))
      f
   )
)
(write-line "Factorial of 5 without recursion")
(write (fact_norm 5))
(terpri)
;;;Factorial with Recursion
(defun factorial (n)
  
(if (= n 1)
 1
 (* n (factorial (- n 1)))))

(write-line "Factorial of 4 with recursion")
(write (factorial 4))
(terpri)
;;;Finding nth element of list

(defun n_list(n lst)
       (let((count 1))
           (loop
               (cond((equal count n)(return (car lst))))
               (setq count (+ count 1))
               (setq lst (cdr lst)))))    
 (write-line "getting a second element from list 10 19 34")              
(write (n_list 2 (list 10 19 34)))
          
          
  
