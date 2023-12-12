program task01
    character(len=9) :: line
    character(len=1) :: current_char
    integer :: file_unit, statut, i

    open(unit = file_unit, file = "./input.txt", status = "old", action = "read", iostat = statut)

    if (statut /= 0) then
        print *, "Couldn't open file"
        stop
    end if

    do while (.true.)
        read(file_unit, *, iostat = statut) line

        if (statut /= 0) exit

        do i = 1, len(line)
            current_char = line(i:i)
            if (current_char == "#") then
                write(*, "(A)", advance="no") "?"
            else
                write(*, "(A)", advance="no") current_char
            end if
        end do
        print *, ""
    end do

    close(file_unit)

end program task01
