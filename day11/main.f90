program main
    use GalaxyModule
    implicit none

    character (len = 100) :: filename
    integer :: result, galaxyNumber, i, j, distance, temp1, temp2, x1, x2, y1, y2, sum
    integer, dimension (:), allocatable :: array

    filename = "./input.txt"

    galaxyNumber = getGalaxyNumber(filename)

    allocate(array(galaxyNumber * 2))

    call registerGalaxies(filename, array)

    sum = 0
    temp1 = 1

    do i = 1, galaxyNumber * 2, 2 ! i -> x1 ; i + 1 -> y1
        temp2 = 1
        do j = 1, galaxyNumber * 2, 2 ! j -> x2 ; j + 1 -> y2
            if (temp1 /= temp2) then
                x1 = array(i)
                x2 = array(j)
                y1 = array(i + 1)
                y2 = array(j + 1)
                distance = abs(x2 - x1) + abs(y2 - y1)
                sum = sum + distance
            end if
            temp2 = temp2 + 1
        end do
        temp1 = temp1 + 1
    end do

    print *, "END... ", sum / 2

end program main
