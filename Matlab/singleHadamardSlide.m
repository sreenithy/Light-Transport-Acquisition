function image=singleHadamardSlide(pixel_size,dimension,light_sequence)
      Blocks=cell(dimension);
      num_of_blocks=dimension(1)*dimension(2);
      location=find(light_sequence)
      light_sequence
      
    for j=1:num_of_blocks
        
        
             if ismember(j,location)
                 Blocks{j}=ones(pixel_size);
             else
                 Blocks{j}=zeros(pixel_size);
             end
    
    end 
      
    image=cell2mat(Blocks);
    image=transpose(image);
%     figure(1)
%     imshow(image)
%     pause
    end