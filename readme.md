# Flow

```C#
class Recommendation {
    private static Recommendation instance;
    public static Recommendation GetRecommendation() {
        if (instance == null) {
            instance = new Recommendation();
        }
        return instance;
    }


    
    public void UpdateCache() {
        newRatingComming()
        
        lock()

        if (ratingUpdated) {
            createCache(ratingUpdated);
        }

        unlock()
    }

    private static bool ratingUpdated = false;

    private void newRatingComming() {
        ghi xuốnng file csv
        ratingUpdated = true;
        return ratingUpdated;
    }

    private void createCache() {
        while (ratingUpdated) {
            ratingUpdated = false;
            //Do dummy things
            lấy file csv ra
            Tạo file cache
        
        }
    }
}
```
