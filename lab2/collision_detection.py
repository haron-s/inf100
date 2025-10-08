import math

def rectangles_overlap(x1,y1,x2,y2,x3,y3,x4,y4):
    x_left1 = min(x1,x2)
    x_right1 = max(x1,x2)

    y_top1 = min(y1,y2)
    y_bottom1 = max(y1,y2)

    x_left2 = min(x3,x4)
    x_right2 = max(x3,x4)

    y_top2 = min(y3,y4)
    y_bottom2 = max(y3,y4)

    if (x_right1 < x_left2 or x_right2 < x_left1 or
        y_bottom1 < y_top2 or y_bottom2 < y_top1):
        return False
    else:
        return True

def distance(x1,y1,x2,y2):
    distance = math.dist((x1,y1), (x2,y2))
    return distance

def circle_overlaps_rectangle(x1, y1, x2, y2, xc, yc, rc):
    x_left, x_right = min(x1, x2), max(x1, x2)
    y_top, y_bottom = min(y1, y2), max(y1, y2)
    
    #sjekker om senter av sirkel er i rektangel
    if x_left <= xc <= x_right and y_top <= yc <= y_bottom:
        return True
    
    #sjekker om senter er utenfor rektangel+radius av sirkel på hver side
    elif (xc < x_left-rc or xc > x_right+rc or
          yc < y_top-rc or yc > y_bottom+rc ):
        return False
    
    #mellom x koordinater av rektangel, sjekker om sirkel sentrum er nærme nok på y aksen
    elif x_left <= xc <= x_right:
        if y_top >= yc >= y_top-rc or y_bottom <= yc <= y_bottom+rc:
            return True
        else:
            return False
    #gjør samme, men for y aksen
    elif y_top <= yc <= y_bottom:
        if x_left >= xc >= x_left-rc or x_right <= xc <= x_right+rc:
            return True
        else:
            return False
    
    #sjekker om sirkelen rører noen av hjørner
    elif (rc >= distance(x_left,y_top,xc,yc) or rc >= distance(x_right,y_top,xc,yc) or
          rc >= distance(x_left,y_bottom,xc,yc) or rc >= distance(x_right,y_bottom,xc,yc)):
        return True
    
    else:
        return False

def test_circle_overlaps_rectangle():
    print('Tester circle_overlaps_rectangle... ', end='')
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 2.5, 2) is True # på midten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 8, 3, 2) is False # langt utenfor
    assert circle_overlaps_rectangle(0, 0, 5, 5, 2.5, 7, 2.01) is True # på kanten
    assert circle_overlaps_rectangle(0, 5, 5, 0, 5.1, 5.1, 1) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 8.99, 5) is True # på hjørnet
    assert circle_overlaps_rectangle(0, 0, 5, 5, 8, 9.01, 5) is False # bare nesten
    print('OK')

test_circle_overlaps_rectangle()