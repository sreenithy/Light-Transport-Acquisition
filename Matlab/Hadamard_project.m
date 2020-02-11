% Code to generate Hadamard projection video file
close all,clear all;clc
image_size=[256 256];
%image_size=[1600 1200];
pixel_size=[16 16];
frame_rate=1;
%pixel_size=[160 120];

dimension=image_size./pixel_size

%  dimension=[4 4];
total_pixels=dimension(1)*dimension(2);

n=log(total_pixels)/log(2);

H=1;
for i=1:n
   
    H=[H H;H -H]
end
H
Hpos=transpose(H);
Hpos(Hpos<0)=0;
Hneg=transpose(H);
Hneg(Hneg>0)=0;
Hneg=-Hneg;

% 
% % rng(1)
% % T=rand(2^n);
% 
% cpos=T*Hpos;
% cneg=T*Hneg;
% 
% c=cpos-cneg;
% T_est=c*inv(H);

% norm(T-T_est)

writerObj_pos=VideoWriter('Hadamard_20fps_256_16_pos.mp4','MPEG-4');
writerObj_pos.FrameRate=frame_rate;
open(writerObj_pos);

writerObj_neg=VideoWriter('Hadamard_20fps_256_16_neg.mp4','MPEG-4');
writerObj_neg.FrameRate=frame_rate;
open(writerObj_neg);

%  figure
%  subplot(1,2,1)
%  imagesc(Hpos)
%  pause
%  subplot(1,2,2)
%  imagesc(Hneg)
%  pause

for i=1:total_pixels
    
    pos_sequence=Hpos(i,:);
    pos_image=singleHadamardSlide(pixel_size,dimension,pos_sequence);
    
    neg_sequence=Hneg(i,:);
    neg_image=singleHadamardSlide(pixel_size,dimension,neg_sequence);
    

    
   writeVideo(writerObj_pos,pos_image);
   writeVideo(writerObj_neg,neg_image);
    
%     figure(100)
%     imshow(image);

end

    figure(1)
    subplot(1,2,1)
    title('positive projection')
    
    imagesc(pos_image)
    pause
    subplot(1,2,2)
    title('negtive projection')
    imagesc(neg_image)
close(writerObj_pos)
close(writerObj_neg)