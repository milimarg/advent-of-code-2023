module GalaxyModule
    implicit none
    public :: getGalaxyNumber
    public :: registerGalaxies

contains

    function getGalaxyNumber(filename) result(number)
        character (len = 100), intent(in) :: filename
        character (len = 100) :: line
        character (len = 1) :: current_char
        integer :: file_unit, statut, index, number, lineLen

        open(unit = file_unit, file = filename, status = "old", action = "read", iostat = statut)

        if (statut /= 0) then
            print *, "Couldn't open file"
            stop
        end if

        number = 0

        do while (.true.)
            read(file_unit, *, iostat = statut) line
            if (statut /= 0) exit
            lineLen = len_trim(line)
            do index = 1, lineLen
                current_char = line(index:index)
                !write (*, "(A)", advance = "no"), current_char
                if (current_char == "#") then
                    number = number + 1
                end if
            end do
            !print *, ""
        end do
        close(file_unit)
    end function getGalaxyNumber

    subroutine registerGalaxies(filename, array)
        character (len = 100), intent(in) :: filename
        character (len = 100) :: line
        character (len = 1) :: current_char
        integer :: file_unit, statut, index, j, moveIndex, result, lineLen
        integer, dimension (:), allocatable, intent(inout) :: array

        open(unit = file_unit, file = filename, status = "old", action = "read", iostat = statut)

        if (statut /= 0) then
            print *, "Couldn't open file"
            stop
        end if

        j = 1
        moveIndex = 1

        do while (.true.)
            read(file_unit, *, iostat = statut) line
            if (statut /= 0) exit
            lineLen = len_trim(line)
            do index = 1, lineLen
                current_char = line(index:index)
                if (current_char == "#") then
                    array(moveIndex) = index
                    array(moveIndex + 1) = j
                    moveIndex = moveIndex + 2
                else
                end if
            end do
            j = j + 1
        end do

        close(file_unit)
    end subroutine registerGalaxies

end module GalaxyModule
