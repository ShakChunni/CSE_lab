
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10      ; var_name data_type value
;b db 6
var db ?
            ; DATA SEGMENT .. FOR VARIABLES ,string,array
msg db "Enter a Hex number: $"  ; last character of string is $
msg1 db "In octal it is: $"
.CODE            



 
MAIN PROC     ; procedure
    
MOV AX,@DATA    ; AX REGISTERS
MOV DS,AX 
; take a hexadecimal number from A to F as input form the user and
;display the octal equivalent of the number in the next line       
    lea dx, msg
    mov ah,9
    int 21h 
    
    
    mov ah,1     ; single character input
    
    int 21h 
    sub al,1Dh
    
    ;mov var,bl 
    
         ; input value is stored in al in hex
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

            
    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    