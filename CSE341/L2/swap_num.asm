
.MODEL SMALL 

.STACK 100H ; SIZE OF STACK SIZE .. H =HEX

.DATA

a db 10      ; var_name data_type value
b db 6
            ; DATA SEGMENT .. FOR VARIABLES

.CODE            



 
MAIN PROC     ; procedure
    
MOV AX,@DATA    ; AX REGISTERS
MOV DS,AX  
     
    mov al,5    
    mov bl,3
    add al,bl   ; a=a+b
    sub bl,al   ; b=b-a-b=-a
    add al,bl   ; a+b-a=b
    neg bl      ; -a=a
     
     
     
     
    ;mov ah,1
    ;int 21h
    ;mov dl,al
    ;mov ah,2
    ;int 21h
     
    ;MOV al,10
    ;mov bl,6
    ;sub al,bl
    ;inc al   ; add al,1 same thing   
    ;dec al 
    ;mov al,a
    ;mov ah,b
    ;add al,ah
    ;mov al,a  
    
                ; for 8 bit multiplication one number must be in al
    ;mov al,6
    ;mov bl,6    ; the result will be stored in ax
    ;mul bl;                                              
                ; for 16 bit multiplication one number must be in ax
                ; the result will be stored in dx(16 bit higher msb) and ax( 16 bit lower lsb)
    
                
                ; the divident is 16 bit and must be in AX 
                ;the 8 bit quotient(result) is in al and 8 bit remainder will be stored in ah
    ;mov ax,21
    ;mov bl,4
    ;div bl      
                ; the divident is 32 bit and in DX(msb-16 bit): AX(lsb-16)
                ; the quotient is in ax and the 16 bit remainder is in dx               
    
    
MOV AX,4C00H
INT 21H
MAIN ENDP
    END MAIN  
    

    