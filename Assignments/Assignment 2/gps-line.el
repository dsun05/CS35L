(defun gps-line ()
  "Print the current buffer line number and narrowed line number of point."
  (interactive)
  (let ((total (count-matches "\n" (point-min) (point-max)))
        (n (line-number-at-pos)))
    (message "Line %d/%d" n total)))
