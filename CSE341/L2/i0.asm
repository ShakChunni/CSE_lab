
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10      ; var_name data_type value
b db 6
var db ?
            ; DATA SEGMENT .. FOR VARIABLES ,string,array
msg db "Hello world$"  ; last character of string is $

.CODE            



 
MAIN PROC     ; procedure
    
MOV AX,@DATA    ; AX REGISTERS
MOV DS,AX 
    ;mov ah,1     ; single character input and output
    ;int 21h      ; input value is stored in al
    ;mov ah,2
;    mov dl,51h  ; dl gets printed as output   
;    int 21h 
;    mov dl,51h
;    mov dl,0Ah
;    int 21h 
;    mov dl,1
;    int 21h   

; string output
                        ; LEA= load effective address
 lea dx,msg  ; dx is fixed for string storation
 mov ah,9
 int 21h
            
    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    