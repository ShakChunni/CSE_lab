
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10      ; var_name data_type value
;b db 6
var db ?
            ; DATA SEGMENT .. FOR VARIABLES ,string,array
msg db "Enter a value:$"
msg2 db "Output: Sum is $"  ; last character of string is $

.CODE            



 
MAIN PROC     ; procedure
    
MOV AX,@DATA    ; AX REGISTERS
MOV DS,AX 

    lea dx,msg  ; dx is fixed for string storation
    mov ah,9
    int 21h
    mov ah,1
    int 21h
    sub al,30h
    ; input in al
    mov dl,0Ah
    mov cl,al
    mov ch,0
    mov ah,2
    int 21h
    
    mov bl,0 
    mov ah,2
     mov dl,0Dh
    int 21h
    repeat:
    mov ah,1
    int 21h
    sub al,30h
    add bl,al
    mov ah,2
    mov dl,0Ah
    int 21h
    mov dl,0Dh
    int 21h
    
 
;     mov ah,1
;     int 21h
;     add bl,al
   loop repeat 
   lea dx,msg2  ; dx is fixed for string storation
    mov ah,9
    int 21h 
   mov dl,bl
   add dl,30h
   mov ah,2
   int 21h 
   
     
         
    
 
            
    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    