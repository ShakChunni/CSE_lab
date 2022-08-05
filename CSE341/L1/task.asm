
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10
b db 6
            ; DATA SEGMENT .. FOR VARIABLES

.CODE            



 
MAIN PROC     ; procedure
    
MOV AX,@DATA    ; AX REGISTERS
MOV DS,AX  
;task-1 
    in ax,27h
    mov bx,ax 
;task-2
    mov al,5
    mov ah,6
    ;mov bl,al
    ;mov al,ah
    ;mov ah,bl
;task-3
    ;add ah,al  
;task-4

;task-5 
    add al,ah
    sub ah,al
    add al,ah
    neg ah
    
    
              
    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    