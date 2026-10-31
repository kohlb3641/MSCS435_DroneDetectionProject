labelDir = 'C:\Users\kohlb3641\OneDrive - University of Wisconsin-Stout\Desktop\Assignments\MSCS435\project1\unfiltered_data\Data\Video_V';
outFile  = 'all_labels.csv';

files = dir(fullfile(labelDir, '*.mat'));
fid = fopen(outFile, 'w');
fprintf(fid, 'label_file,video,row,time_s,class,x,y,w,h\n');

for i = 1:numel(files)
    S  = load(fullfile(labelDir, files(i).name), 'gTruth');
    gt = S.gTruth;

    % Video file name the labels belong to
    try
        src = gt.DataSource.Source;
        if iscell(src), src = src{1}; end
        [~, vn, ve] = fileparts(src);
        vname = [vn ve];
    catch
        vname = '';
    end

    T = gt.LabelData;
    if istimetable(T)
        t = seconds(T.Properties.RowTimes);
    else
        t = nan(height(T), 1);
    end
    classes = T.Properties.VariableNames;

    for r = 1:height(T)
        for c = 1:numel(classes)
            v = T{r, c};
            if iscell(v), v = v{1}; end
            if isstruct(v)                      % labels with attributes
                if isempty(v), continue; end
                v = vertcat(v.Position);
            end
            if isempty(v), continue; end
            for k = 1:size(v, 1)                % only one row per box
                fprintf(fid, '%s,%s,%d,%.4f,%s,%.2f,%.2f,%.2f,%.2f\n', ...
                    files(i).name, vname, r, t(r), classes{c}, ...
                    v(k,1), v(k,2), v(k,3), v(k,4));
            end
        end
    end
    fprintf('%d/%d  %s  (%d rows)\n', i, numel(files), files(i).name, height(T));
end
fclose(fid);