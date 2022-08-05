.MODEL SMALL
 
.STACK 100H

.DATA
a db 5
b db 5 dup(?)
c dw 12
.CODE
MAIN PROC

;iniitialize DS

MOV AX,@DATA
MOV DS,AX
 
; enter your code here
 mov al,5
 mov bh,10
 ;add al,ah
 ;sub al,ah 
 ;inc al
 ;dec al   
            ; 8 bit or byte multiplication
 ;mul bh   ; one number must be in al and the result will be stored in ax  
 
            ; 16 bit or word multiplication
 ;mov bx,5; 
 ;mul bx;    ; one number must be in ax and the result will be stored in ax
            ; and dx , the lower 16 bits in ax, higher in dx 

            ; 8 bit divisor
               ; the dividend is 16 bit and must be in ax
               ; after division 8 bit quotient in al
               ; 8 bit remainder in ah
 mov ax,40
 mov bh, 6
 div bh     
            ; 16 bit divisor 
                ; the dividend is 32 bit and in dx:ax
                ; after division 16 bit quotient in ax
                ; 16 bit remainder in dx
 


 

;exit to DOS
               
MOV AX,4C00H
INT 21H

MAIN ENDP
    END MAIN
