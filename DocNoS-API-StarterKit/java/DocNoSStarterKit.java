import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import org.json.JSONObject;
import org.json.JSONArray;

public class DocNoSStarterKit {

    private static final String URL_CREATE = "https://blockchains.web-lab.at/docnos3-api/create/";
    private static final String URL_VERIFY = "https://blockchains.web-lab.at/docnos3-api/verify/";
    private static final String API_TOKEN = "starterKit/test/44ede16fa685b3be6b874a01a21f8fff4c6f613a4f3f6b169179fe59956bb914"; // Replace with your actual API token
    private static final String DEFAULT_CONTENT = "This is just some content, which is used as input example ... 123abcxyz java";

    public static void main(String[] args) {
        createNotarization();
        verifyNotarization();
    }

    private static void createNotarization() {
        System.out.println("------------------------------------------------");
        System.out.println("DocNos - Test ... create");

        String sha256Hash = calculateHash(DEFAULT_CONTENT, "SHA-256");
        String sha512Hash = calculateHash(DEFAULT_CONTENT, "SHA-512");

        String uuid = "12345678-5f7c-4eb2-9344-b35943815ed5";

        JSONObject hashes = new JSONObject();
        hashes.put("sha256", sha256Hash);
        hashes.put("sha512", sha512Hash);

        JSONObject request = new JSONObject();
        request.put("id", uuid);
        request.put("hashes", hashes);
        request.put("remarks", "sent from starterKit (Java) 0.7.0");

        String postData = request.toString();
        System.out.println("JSON-Request:");
        System.out.println(postData);
        System.out.println("------------------------------------");

        try {
            URL url = new URL(URL_CREATE);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setRequestProperty("Content-Type", "application/json");
            connection.setRequestProperty("Accept", "application/json");
            connection.setRequestProperty("Content-Length", Integer.toString(postData.length()));
            connection.setRequestProperty("X-ApiToken", API_TOKEN);
            connection.setDoOutput(true);

            try (OutputStream os = connection.getOutputStream()) {
                byte[] input = postData.getBytes(StandardCharsets.UTF_8);
                os.write(input, 0, input.length);
            }

            int responseCode = connection.getResponseCode();
            System.out.println(connection);
            System.out.println("Response Code : " + responseCode);

            try (BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                System.out.println("RESULT: " + response.toString());
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void verifyNotarization() {
        System.out.println("------------------------------------------------");
        System.out.println("DocNos for - Test ... verify");

        String sha256HashToVerify = calculateHash(DEFAULT_CONTENT, "SHA-256");

        try {
            URL url = new URL(URL_VERIFY + "?hash=sha256:" + sha256HashToVerify);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setRequestProperty("Accept", "application/json");
            connection.setRequestProperty("X-ApiToken", API_TOKEN);

            System.out.println(connection.getHeaderFields());
            System.out.println(connection);
            try (BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream(), StandardCharsets.UTF_8))) {
                StringBuilder response = new StringBuilder();
                String responseLine;
                while ((responseLine = br.readLine()) != null) {
                    response.append(responseLine.trim());
                }
                String rawResult = response.toString();
                System.out.println("Raw RESULT: " + rawResult);

                JSONObject parsedResponse = new JSONObject(rawResult);
                System.out.println("Beautified RESULT: " + parsedResponse.toString(2));
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String calculateHash(String input, String algorithm) {
        try {
            MessageDigest digest = MessageDigest.getInstance(algorithm);
            byte[] hash = digest.digest(input.getBytes(StandardCharsets.UTF_8));
            StringBuilder hexString = new StringBuilder();
            for (byte b : hash) {
                String hex = Integer.toHexString(0xff & b);
                if (hex.length() == 1) {
                    hexString.append('0');
                }
                hexString.append(hex);
            }
            return hexString.toString();
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        }
    }
}