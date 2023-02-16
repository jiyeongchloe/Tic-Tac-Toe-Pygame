

Class Board:
    import pygame, sys
    import numpy as np
    pygame.init()

    Global WIDTH = 600
    Global HEIGHT = 600
    Global LINE_WIDTH = 15
    Global WIN_LINE_WIDTH = 15
    Global BOARD_ROWS = 3
    Global BOARD_COLS = 3
    Global SQUARE_SIZE = 200
    Global CIRCLE_RADIUS = 60
    Global CIRCLE_WIDTH = 15
    Global CROSS_WIDTH = 25
    Global SPACE = 55

    Global BG_COLOR = (20, 200, 160)
    Global LINE_COLOR = (23, 145, 135)
    Global CIRCLE_COLOR = (239, 231, 200)
    Global CROSS_COLOR = (66, 66, 66)

    screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
    pygame.display.set_caption( 'TIC TAC TOE' )
    screen.fill( BG_COLOR )

    board = np.zeros( (BOARD_ROWS, BOARD_COLS) )

    def draw_lines():
        
        pygame.draw.line( screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH )
        
        pygame.draw.line( screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH )

        pygame.draw.line( screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH )

        pygame.draw.line( screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH )

    def draw_figures():
	for row in range(BOARD_ROWS):
		for col in range(BOARD_COLS):
			if board[row][col] == 1:
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, CIRCLE_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )	
				pygame.draw.line( screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH )

    def mark_square(row, col, player):
        board[row][col] = player

    def available_square(row, col):
        return board[row][col] == 0

    def is_board_full():
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == 0:
                    return False
        return True
    
        


