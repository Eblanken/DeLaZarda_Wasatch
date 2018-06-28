% Erick Blankenberg
% DeLaZerda Research
% Wasatch Writer
% Calibration Data

clear all;
close all;

% Iterates over all of the image files we have, does not currently consider
% connected tile edges.

% Functions and constants

% -> Scanner Setup
numCols = 8; % Number of columns of images in the merged document
numRows = 8; % Number of rows of images in the merged document
totalColLength = 10.22; % (mm) X dimension of the merged image set
totalRowLength = 11.99; % (mm) Y dimension of the merged image set

% -> Programmed Units
wUnits_Cols = 800; 
wUnits_Rows = 400;

% -> Gaussian Approximation
gaussian = @(a, x) a(1).*exp(-(x-a(2)).^2./(2*a(3).^2))+a(4); % Format is a = [magnitude, center, variance, baseline]
initialMagnitude = 0.1; % mm
initialVariance = 0.25; % mm

% -> Peak Detection 
expectedDistanceMinimum_Col = 0.3; % mm (rough guess for findpeaks)
expectedWidthMaximum_Col = 0.15; % mm (rough guess for findpeaks)
expectedProminanceMinimum_Col = 4; % greyscale / 255 (rough guess for findpeask)
plotAll_Col = false; % set to true to plot peaks for each image

expectedDistanceMinimum_Row = 0.15;% mm (rough guess for findpeaks)
expectedWidthMaximum_Row = 0.075; % mm (rough guess for findpeaks)
expectedProminanceMinimum_Row = 4; % greyscale / 255 (rough guess for findpeak)
plotAll_Row = false; % set to true to plot peaks for each image

% Iterates over images
% Positions of lines
colOutput = []; % format is [xPositionGlobal, sourceRowIndex];...
rowOutput = []; % format is [yPositionGlobal, sourceColumnIndex];...
% Differences between positions
colDiffs = []; % format is [xPositionGlobal, differenceMagnitude, sourceRowIndex]
rowDiffs = []; % format is [yPositionGlobal, differenceMagnitude, sourceColumnIndex]
for rowIndex = 1:numRows
    for colIndex = 1:numCols
        fileString = sprintf('/Users/ANoSenseSolution/Documents/MATLAB/DeLaZerda/Writer/NewScans/R%d_C%d.tif', rowIndex, colIndex);
        if(exist(fileString, 'file'))
            image = imread(fileString);
            normedData = image; %(image)./((max(max(image)))/255);

            % Column cross section
            colNormed = -1.*sum(normedData, 1)./size(normedData, 1);
            globalPositionStart = (colIndex - 1) * (totalColLength / numCols);
            colSpace = (linspace(0, 1.48, length(colNormed)) + globalPositionStart)';
            % Inverted to use findpeaks on valleys
            globalPositionStart = (colIndex - 1) * (totalColLength / numCols);
            [pks_col,locs_col] = findpeaks(colNormed, colSpace, 'MinPeakDistance', expectedDistanceMinimum_Col, 'MaxPeakWidth', expectedWidthMaximum_Col, 'MinPeakProminence', expectedProminanceMinimum_Col);
            pks_col = pks_col .* -1;
            if(plotAll_Col)
                figure;
                hold on;
                findpeaks(colNormed, colSpace, 'MinPeakDistance', expectedDistanceMinimum_Col, 'MaxPeakWidth', expectedWidthMaximum_Col, 'MinPeakProminence', expectedProminanceMinimum_Col);
                titleText = sprintf('Column Section for R%d-C%d.tiff',rowIndex, colIndex);
                title(titleText);
                hold off;
            end
            indexVector = ones(length(locs_col), 1).*rowIndex;
            colOutput = [colOutput; [locs_col, indexVector]];
            locs_col
            diff(locs_col)
            colDiffs = [colDiffs; [0.5 * (locs_col(1:end-1) + locs_col(2:end)), diff(locs_col), indexVector(1:(end - 1))]];
            %{
            localOutput = []; TODO fix gaussian fit % TODO fix gaussian fit
            for index = 1:length(locs)
                initialGuess = [initialMagnitude, locs(index), initialVariance, pks(index)];
                result = fminsearch(@(a) sum(sum(colNormed - gaussian(a, colSpace)))^2, initialGuess);
                localOutput = [localOutput; result];
            end
            %}
            
            % Row cross section
            rowNormed = -1.*sum(normedData, 2)./size(normedData, 2);
            rowNormed = rowNormed';
            globalPositionStart = (rowIndex - 1) * (totalRowLength / numRows);
            rowSpace = (linspace(0, 1.48, length(rowNormed)) + globalPositionStart)';
            % Inverted to use findpeaks on valleys
            [pks_row,locs_row] = findpeaks(rowNormed, rowSpace, 'MinPeakDistance', expectedDistanceMinimum_Row, 'MaxPeakWidth', expectedWidthMaximum_Row, 'MinPeakProminence', expectedProminanceMinimum_Row);
            pks_row = pks_row .* -1;
            if(plotAll_Row)
                figure;
                hold on;
                findpeaks(rowNormed, rowSpace, 'MinPeakDistance', expectedDistanceMinimum_Row, 'MaxPeakWidth', expectedWidthMaximum_Row, 'MinPeakProminence', expectedProminanceMinimum_Row);
                titleText = sprintf('Row Section for R%d-C%d.tiff',rowIndex, colIndex);
                title(titleText);
                hold off;
            end
            indexVector = ones(length(locs_row), 1).*colIndex;
            rowOutput = [rowOutput; [locs_row, indexVector]];
            rowDiffs = [rowDiffs; [0.5 * (locs_row(1:end-1) + locs_row(2:end)), diff(locs_row), indexVector(1:(end - 1))]];
            %{
            localOutput = [];
            for index = 1:length(locs)
                initialGuess = [initialMagnitude, locs(index), initialVariance, pks(index)];
                result = fminsearch(@(a) sum(sum(colNormed - gaussian(a, colSpace)))^2, initialGuess);
                localOutput = [localOutput; result];
            end
            %}
            %colOutput = [colOutput, localOutput];
        else 
            errorText = sprintf('Unable to find file %s\n', fileString);
            fprintf(errorText);
        end
    end
end
% Plots spacing tolerance
figure
hold on;
colDifferences = ((colDiffs(:,2))./wUnits_Cols).^-1;
rowDifferences = ((rowDiffs(:,2))./wUnits_Rows).^-1;
range = min([colDifferences; rowDifferences]):1:max([colDifferences; rowDifferences]);
pd_col = fitdist(colDifferences,'Kernel','Kernel','epanechnikov');
y_col = pdf(pd_col, range);
plot(range, y_col, 'LineWidth', 2, 'displayName', 'Column Spacing (Wasatch Units / MM)');
%pd_row = fitdist(rowDifferences,'Kernel','Kernel','epanechnikov');
%y_row = pdf(pd_row, range);
%plot(range,y_row,'LineWidth',2, 'displayName', 'Row Spacing (Wasatch Units / MM)');
legend('show');
xlabel('Wasatch Units');
ylabel('Density');
title('Averaged Wasatch Units / MM From Line Division Data');
hold off;

% Plots spatial distribution of spacing
% -> Columns
figure;
hold on;
for index = 1:numRows
    curLocations = nonzeros(colDiffs(:, 1).*(colDiffs(:, 3) == index));
    curSpaces = nonzeros(colDiffs(:, 2).*(colDiffs(:, 3) == index));
    labelText = sprintf('Row %d', index);
    plot(curLocations, curSpaces, 'displayName', labelText);
end
title('Spacing In MM Over Column Range');
legend('show');
xlabel('X Position (mm)');
ylabel('Difference (mm)');
hold off;

% -> Rows
figure;
hold on;
for index = 1:numCols
    curLocations = nonzeros(rowDiffs(:, 1).*(rowDiffs(:, 3) == index));
    curSpaces = nonzeros(rowDiffs(:, 2).*(rowDiffs(:, 3) == index));
    labelText = sprintf('Column %d', index);
    plot(curLocations, curSpaces, 'displayName', labelText);
end
title('Spacing In MM Over Row Range');
legend('show');
xlabel('Y Position (mm)');
ylabel('Difference (mm)');
hold off;
