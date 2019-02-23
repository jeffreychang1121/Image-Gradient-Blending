import drawMask as dm

def maskImage(img):
    mask, _ = dm.draw_mask(img)

    return mask