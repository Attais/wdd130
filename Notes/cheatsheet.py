# HTML Cheatsheet 


#CSS Cheetsheet
    
    #Flex box cheetsheet
       
         #justify-content - adjust horizontally
            #flex-start - align to left side of container
            #flex-end - align to right side of container
            #center - align to horizontal center
            #space-between - items display with equal space between them
            #space-around - items displace with equal space around them

        #align-content - sets how much space is between lines
            #flex-start - lines bunched at top
            #flex-end - lines bunched at bottom
            #center - packed at center
            #space-between - equal space between lines
            #space-around - equal space around lines
            #stretch - lines stretched to fill container

        #align-items - adjust vertically
            #flex-start - align to the top of the container
            #flex-end - align to the bottom of the container
            #center - align to vertical center
            #baseline - items display at baseline of container (?)
            #stretch - items are stretched to fit container (?)
                #can use align-self for individual items

        #flex-direction - adjusts order 
            #row - items placed in same direction as text
            #row-reverse - items placed opposite text direction
            #column - items placed top to bottom
            #column-reverse - items placed bottom to top

        #order - changes the "priority" of an item in a list, moving it forward or backward
            #"Sometimes reversing the row or column order of a container is not enough. In these cases, we can apply the order property to individual items. By default, items have a value of 0, but we can use this property to also set it to a positive or negative integer value (-2, -1, 0, 1, 2)"
            #Higher number = further back
            #item is classified as ."item," as in .yellow

        #flex-wrap - sets rules for wrapping text 
            #nowrap - every item fits on a single line
            #wrap - items wrap to additional lines
            #wrap-reverse - items wrap in reverse

        #flex-flow - flex-direction + flex-wrap
            #uses two identifiers, such as row wrap or column wrap
